class sequence_unique:
    """ 
    Object to store the sequence information like: **counts**, **sequence**, **id** 
    """
    def __init__(self,idx,seq):
        self.idx = idx
        self.seq = seq
        self.group = {}
    def add_exp(self,gr,exp):
        """Function to add the counts for each sample

        :param gr: name of the sample
        :param exp: counts of sample **gr**

        :returns: dict with key,values equally to name,counts.
        """
        self.group[gr] = exp

class cluster_info_obj:
    """
    Object containing information about clusters(:code:`clus_obj`), 
    positions(:code:`positions`) and sequences(:code:`sequences`)
    """
    def __init__(self,clus_obj,clus_id,loci_obj,seq_obj):
        self.clus = clus_obj
        self.clusid = clus_id
        self.loci = loci_obj
        self.seq = seq_obj

#class pairs:
#        def __init__(self):
#                self.p2 = {}
#                self.st = {}
#        def set_dist(self,p,d,st):
#                self.p2[p] = d
#                self.st[p] = st

class sequence:
    """
    Object with information about sequences, counts, size, position, id and score
    """
    def __init__(self, seq,freq,seq_id):
        self.seq = seq
        self.freq = freq
        self.len = len(seq)
        self.pos = []
        self.id = seq_id
        self.score = 0
    def add_pos(self,pos_id):
        self.pos.append(pos_id)

class position:
    """
    Object with information about position: chr,start,end,strand
    as well, with annotation information throuhg :code:`dbannotation` object 
    """
    def __init__(self,idl, chr,start,end,strand):
        self.idl = idl
        self.chr = chr
        self.start = int(start)
        self.end = int(end)
        self.strand = strand
        self.db_ann = {}
    def add_db(self,db,ndb):
        self.db_ann[db] = ndb


class annotation:
    """
    Object with information about annotation: database, name of the feature, strand,
    distance to 5' end, distance to 3' end
    """
    def __init__(self,db,name,strand,to5,to3):
        self.db = db
        self.name = name
        self.strand = strand
        self.to5 = to5
        self.to3 = to3

class dbannotation:
    """
    Object with information about annotation: containg one dict that 
    store all features for each database type
    """
    def __init__(self,na):
        self.ann = {}
    def add_db_ann(self,ida,ndba):
        self.ann[ida] = ndba
      
class cluster:
    """
    Object with cluster information. This is the main object.
    """
    def __init__(self, id):
        self.id = id
        self.idmembers = {}
        #self.loci = {}
        self.locimax = 0
        self.locilen = {}
        self.loci2seq = {}
        #self.pairs = {}
        #self.dist_pair = {}
        self.ref = 0
        self.score = 0
        self.showseq = ""
        self.showseq_plain = ""
        self.toomany = 0
    def set_ref(self,r):
        self.ref = r
    #def addpair(self,p1,p2,d,s):
    #            if not (self.pairs.has_key(p1)):
    #                    self.pairs[p1] = pairs()
    #                    self.dist_pair[p1] = 1
    #            self.pairs[p1].set_dist(p2,d,s)
    #            self.dist_pair[p1]+= 1
    def add_id_member(self, ids, idl):
        lenid = len(ids)
        self.locilen[idl] = lenid
        for s in ids:
            self.idmembers[s] = 0
            if not idl in self.loci2seq:
                self.loci2seq[idl] = []
            self.loci2seq[idl].append(s)
        if lenid > self.locimax:
            self.locimax = lenid
    #def addloci(self,idl,np):
    #    self.loci[idl] = 1
     


class bcolors:
    HEADER  =  '\033[95m'
    OKBLUE  =  '\033[94m'
    OKGREEN  =  '\033[92m'
    WARNING  =  '\033[93m'
    FAIL  =  '\033[91m'
    ENDC  =  '\033[0m'

class bedaligned:
        def __init__(self,l):
            l = l.strip()
            cols = l.split("\t")
            self.chr = cols[0]
            self.start = cols[1]
            self.end = cols[2]
            self.name = cols[3]
            self.att = cols[4]
            self.strand = cols[5]

class mergealigned:
        def __init__(self,l):
                self.chr = l[0]
                self.strand = l.strand
                self.start = l.start
                self.end = l.end
                self.names = list(l.name.split(","))
                self.loci = l.score.split(",")
