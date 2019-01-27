class Node(object):
    "Generic tree node."
    def __init__(self, name):
        self.name = name
        self.child = {}

        
        
        
class HomeAddressTree(object):
    '''
    This class creates a address tree form
    the provided address dictionary
    A random walk on tree provides => country.province.district.VRD.ward
    '''
    def __init__(self,country,ID):
        self.root = Node(country,ID)
        
    def set_province(self,province,PID):
        self.root.child.update({province:Node(province,PID)})
            
    def set_district(self,province,district,DID):
        self.root.child[province].child.update({district:Node(district,DID)})
        
    def set_VRD(self,province,district,VRD,VID):
        self.root.child[province].child[district].child.update({VRD:Node(VRD,VID)})
        
    def set_ward(self,province,district,VRD,ward,WID):
         self.root.child[province].child[district].child[VRD].child.update({ward:Node(ward,WID)})
            
    
    
    
    
    
    
    