import os, sys
from rdkit import *


def grid_in():
    with open("grid.in", "w") as fh:
        fh.write(
            "ligand_atom_file                                             ./actives_final.mol2
            "limit_max_ligands                                            no
            "skip_molecule                                                no
            "read_mol_solvation                                           no
            "calculate_rmsd                                               no
            "use_database_filter                                          no
            "orient_ligand                                                yes
            automated_matching                                           yes
            receptor_site_file                                           selected_spheres.sph
            max_orientations                                             500
            critical_points                                              no
            chemical_matching                                            no
            use_ligand_spheres                                           no
            use_internal_energy                                          yes
            internal_energy_rep_exp                                      12
            flexible_ligand                                              yes
            user_specified_anchor                                        no
            limit_max_anchors                                            no
            min_anchor_size                                              40
            pruning_use_clustering                                       yes
            pruning_max_orients                                          100
            pruning_clustering_cutoff                                    100
            pruning_conformer_score_cutoff                               25.0
            use_clash_overlap                                            no
            write_growth_tree                                            no
            bump_filter                                                  no 
            score_molecules                                              yes
            contact_score_primary                                        no
            contact_score_secondary                                      no
            grid_score_primary                                           yes
            grid_score_secondary                                         no
            grid_score_rep_rad_scale                                     1
grid_score_vdw_scale                                         1
grid_score_es_scale                                          1
grid_score_grid_prefix                                       grid
multigrid_score_secondary                                    no
dock3.5_score_secondary                                      no
continuous_score_secondary                                   no
descriptor_score_secondary                                   no
gbsa_zou_score_secondary                                     no
gbsa_hawkins_score_secondary                                 no
SASA_descriptor_score_secondary                              no
amber_score_secondary                                        no
minimize_ligand                                              yes
minimize_anchor                                              yes
minimize_flexible_growth                                     yes
use_advanced_simplex_parameters                              no
simplex_max_cycles                                           1
simplex_score_converge                                       0.1
simplex_cycle_converge                                       1.0
simplex_trans_step                                           1.0
simplex_rot_step                                             0.1
simplex_tors_step                                            10.0
simplex_anchor_max_iterations                                500
simplex_grow_max_iterations                                  500
simplex_grow_tors_premin_iterations                          0
simplex_random_seed                                          0
simplex_restraint_min                                        no
atom_model                                                   all
vdw_defn_file                                                /opt/dock6/parameters/vdw_AMBER_parm99.defn
flex_defn_file                                               /opt/dock6/parameters/flex.defn
flex_drive_file                                              /opt/dock6/parameters/flex_drive.tbl
ligand_outfile_prefix                                        anchor_and_grow
write_orientations                                           no
num_scored_conformers                                        1
rank_ligands                                                 no
            
 
    

def run_prgrm():
    lig_lst = glob.glob("mol2")
    for i in lig_lst:
        os.system("sphere_selector rec.sph "+i+"15.0")
        os.system("showbox < box.in")
        os.system("grid -i grid.in -o grid.out")
        
        
        
        
        
    
