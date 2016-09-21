import numpy as np
import pdb

def load_data(file_name):
    data = np.loadtxt(file_name,dtype=str,unpack=True)
    names = data[3:,0]
    pos = data[0,1:].astype(int)
    af_yri = data[1,1:].astype(float)
    af_den = data[2,1:].astype(float)
    haps = data[3:,1:].astype(int)
    return names,pos,af_yri,af_den,haps

def compute_obs(pos,af_yri,af_den,haps,thresh):
    obs_mat = np.zeros(haps.shape,dtype=int)
    for indiv in range(0,haps.shape[0]):
        for pos in range(0,haps.shape[1]):
            obs_mat[indiv,pos] = int(haps[indiv,pos]==1 and af_yri[pos]<=thresh and af_den[pos]>0)            
    return obs_mat

def get_dist_set(pos_list):
    dist_set = set()
    for positions in pos_list:
        dist = [positions[i+1]-positions[i] for i in range(0,len(positions)-1)]
        dist_set.update(dist)
    return dist_set

def write_paramters_to_file(file_name,r,t,m,info_thresh,hmm_thresh,e_01,e_11):
    outfile = open(file_name,'wb')
    outfile.write('parameters:\tm=%f\tt=%d\tr=%E\tinfo_thresh=%f\thmm_thresh=%f\te_01=%E\te_11=%E\n'%(m,t,r,info_thresh,hmm_thresh,e_01,e_11))

def write_tracts_to_file(outfile,name,starts,ends): # write results to outfile
    outfile.write('%s\t' %name)
    for i in range(0,len(starts)):
        outfile.write('%d\t%d\t' %(starts[i],ends[i]))
    outfile.write('\n')