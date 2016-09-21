import hmm_module
import file_manager as fm
import numpy as np
import argparse
import pdb

def posterior_decoding_fb(hmm,obs_mat,positions,names,outfile): # for real data
    # run posterior decoding for each individual
    for i in range(0,obs_mat.shape[0]):
        print 'analyzing %s' %names[i]
        obs = obs_mat[i,:]
        path,probs = hmm.forward_backward_scaled(obs, positions)
        starts,ends = hmm.get_starts_ends(path,positions)
        fm.write_tracts_to_file(outfile,names[i],starts,ends)
        
    # close file
    outfile.close()

def init_hmm(r,t,m,positions,thresh,e_11,e_01):
    # transition and emission probabilities 
    a_01 = r*(t-1)*m
    a_10 = r*(t-1)*(1-m)
    prior = np.array([1-m,m])
    transition = np.array([[1-a_01, a_01],
                           [a_10, 1-a_10]])
    emission = np.array([[1-e_01, e_01],
                         [1-e_11, e_11]])
    
    # for precomputing transition matrices
    dist_set = fm.get_dist_set([positions])

    return hmm_module.HMM(prior, transition, emission, dist_set,thresh)

if __name__=='__main__':
    #params
    r = 2.3e-8 # recomb rate per bp per gen
    t = 1900 # admixture time in generations
    m = 0.02 # admixture proportion
    info_thresh = 0.05 
    hmm_thresh = 0.9 # call tract if posterior probability is higher than this value
    e_11 = .050702 # from simulation
    e_01 = 7.405e-4 # from simulation
    
    #read command line arguments
    parser = argparse.ArgumentParser(description="infer admixure tracts")
    parser.add_argument("-i", type=str, dest="i",help="absolute path of the input file")
    parser.add_argument("-o", type=str, dest="o",help="absolute path of the output path")
    parser.add_argument("-r", type=float, dest="r",help="recombination rate (per bp per generation)", default=r)
    parser.add_argument("-t", type=float, dest="t",help="admixture time (in generations)", default=t)
    parser.add_argument("-m", type=float, dest="m",help="admixture proportion", default=m)
    parser.add_argument("-it", type=float, dest="it",help="threshold at which to call a site informative", default=info_thresh)
    parser.add_argument("-ht", type=float, dest="ht",help="confidence level at which to call tracts", default=hmm_thresh)
    args=parser.parse_args()    
    r,t,m,info_thresh,hmm_thresh,infile_path,outfile_path = args.r,args.t,args.m,args.it,args.ht,args.i,args.o
    
    print "loading data"
    names,positions,af_yri,af_den,haps = fm.load_data(infile_path)
    
    print 'preprocessing data'
    obs_mat = fm.compute_obs(positions,af_yri,af_den,haps,info_thresh)
    
    print 'initializing HMM'
    hmm = init_hmm(r, t, m, positions,hmm_thresh,e_11,e_01)
    
    print 'posterior decoding'
    outfile = open(outfile_path,'wb')
    posterior_decoding_fb(hmm,obs_mat,positions,names,outfile)

    
    