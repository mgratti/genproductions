# Script to read the log files created by calculateXSectionAndFilterEfficiency.sh
# and store them into a file compatible that can be read from nanoMT2

# please copy the logs into a dir logs_bla

# based on ../datasets.txt, read the all logs available in the logs_bla
# in each log identify the the important strings , xsec, filter eff, 
# and write them to file with appropriate convention




import os
import glob
import re



if __name__ == "__main__":



  logs = glob.glob('../*.log')
  f = open('../mc_bkg_2017.txt')


  for line in f:
    if '#' in line or line == '\n': continue
    sample = line.split('/')[1]
    #print 'Working on sample' , sample

    logname = '../xsec_{s}.log'.format(s=sample)
    
    if not os.path.isfile(logname): 
      print 'ERROR do not have a xsec log file for this sample , %s ' %logname
      continue

    flog = open(logname)
    count_match=0
    for fline in flog:
      if 'After matching: total cross section ' in fline:
        #print fline
        count_match += 1
        res = re.search('After matching: total cross section = (.*)\+-', fline)
        xsec = float(res.group(1)) # in pb
        #print xsec

      if 'Filter efficiency (taking into account weights)= ' in fline:
        count_match +=1
        res = re.search(' = (.*) \+- ', fline)
        filtereff = float(res.group(1))
        #print filtereff
        
     
    if count_match != 2:  print 'ERROR could not find xsec and or filter eff in log ', flog, 'for sample ', sample
    else:
      # # Id    # dataset name  cross-section (pb)       #  filter eff. # k-factor 
      print '{id} {name}    {xsec}   {filtereff}   {kfac}'.format(id=' ', name=sample, xsec=xsec, filtereff=filtereff, kfac=1.0)
    
  


