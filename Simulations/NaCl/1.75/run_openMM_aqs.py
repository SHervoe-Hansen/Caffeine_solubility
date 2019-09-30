
# Imports
import sys
import os
from simtk.openmm import app
import simtk.openmm as mm
import openmmtools as mmtools
from parmed import load_file, unit as u
from parmed.openmm import StateDataReporter

print('Loading initial configuration and toplogy')
init_conf = load_file(Caffeine_NaCl_aqs.top', xyz=Caffeine_NaCl_aqs.pdb')

# Creating system
print('Creating OpenMM System')
system = init_conf.createSystem(nonbondedMethod=app.PME, ewaldErrorTolerance=0.0005,
                                nonbondedCutoff=1.2*u.nanometers, constraints=app.HBonds)
                                                    
# Positional restraints
state = 'aqs'
if state == 'iso':
    force = mm.CustomExternalForce("k*((x-x0)^2+(y-y0)^2+(z-z0)^2)")
    force.addGlobalParameter("k", 5.0*u.kilocalories_per_mole/u.angstroms**2)
    force.addPerParticleParameter("x0")
    force.addPerParticleParameter("y0")
    force.addPerParticleParameter("z0")
    for i, atom_cmd in enumerate(init_conf.positions):
        force.addParticle(i, atom_cmd.value_in_unit(u.nanometers))
    system.addForce(force)

# Temperature-coupling by geodesic Langevin integrator (NVT)
integrator = mmtools.integrators.GeodesicBAOABIntegrator(K_r = 3,
                                                         temperature = 298.15*u.kelvin,
                                                         collision_rate = 1.0/u.picoseconds,
                                                         timestep = 2.0*u.femtoseconds
                                                        )

# Pressure-coupling by a Monte Carlo Barostat (NPT)
system.addForce(mm.MonteCarloBarostat(1*u.bar, 298.15*u.kelvin, 25))

platform = mm.Platform.getPlatformByName('CUDA')
properties = {'CudaPrecision': 'mixed', 'CudaDeviceIndex': '0'}

# Create the Simulation object
sim = app.Simulation(init_conf.topology, system, integrator, platform, properties)

# Set the particle positions
sim.context.setPositions(init_conf.positions)

# Minimize the energy
print('Minimizing energy')
sim.minimizeEnergy(tolerance=1*u.kilojoule/u.mole, maxIterations=500000)
    
# Draw initial MB velocities
sim.context.setVelocitiesToTemperature(298.15*u.kelvin)

# Set up the reporters
sim.reporters.append(app.StateDataReporter(sys.stdout, 1000, totalSteps=25000000,
    time=True, potentialEnergy=True, kineticEnergy=True, temperature=True, density=True,
    remainingTime=True, speed=True, separator='	'))

# Set up trajectory reporter
sim.reporters.append(app.DCDReporter('trajectory_aqs.dcd', 1000, append=False))

# Run dynamics
print('Running dynamics! (NPT)')
sim.step(25000000) # 25000000*2 fs = 50 ns
