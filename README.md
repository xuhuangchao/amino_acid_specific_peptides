# amino_acid_specific_peptides

1_groupbyacids: Store the AutoDock docking results in folders named after amino acids, such as alanine, arginine,...

2_read_files: Read the 20 txt files and store the docking results into npy format with a matrix size of 280w * 20 
(280w represents the total number of peptides while there are 20 types of amino acids)

3_process: The specific polypeptide for each amino acid is screened, and the screening rules are:
1) the difference between the largest absolute value of the binding free energy and the second value is greater than or equal to 3 

  e.g. No.241145 is specific for the 9th amino acid, with a minimum binding energy of -6.77kcal/mol and a second binding energy of -3.73kcal/mol. The difference is 3.04kcal/mol. No.241145 polypeptide is 080177202 while the 9th amino acid is histidine

2) only one binding free energy is negative, and the others are 0
