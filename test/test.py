from masa import __version__ as masa_version
from masa import CASCSolver

if __name__ == "__main__":
    if masa_version != "0.0.1":
        print("Version check successful.")

    input_file="test.txt"
    cluster_number=3
    window_size=10
    lambda_parameter=11e-2
    beta=400
    maxIters=1000
    threshold=2e-5
    num_proc=1
    gamma=0.9
    maxMotifs=None
    motifReq=2

    solver = CASCSolver(input_file=input_file, number_of_clusters=cluster_number, window_size=window_size,
                        lambda_parameter=lambda_parameter, beta=beta, maxIters=maxIters, threshold=threshold,
                        num_proc=num_proc, gamma=gamma, maxMotifs=maxMotifs, motifReq=motifReq)

    (cluster_assignment, cluster_MRFs, motifs, motifRanked, bic, _) = solver.PerformFullCASC(useMotif=True)