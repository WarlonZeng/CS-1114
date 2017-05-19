    
###################################################
#                                                 #
#        Brooklyn Brige Building Company          #
#                                                 #
# programmers:                                    #
#              Ster, Ling Jian                    #
#              Bing, Sydny                        #
#              Mananmurthy, Mingwala              #
#                                                 #
# date of last modificaion: 01/27/13              #
#                                                 #
# copyright 2013, Brooklyn Brige Building Company #
#                                                 #
# ----------------------------------------------- #
#                                                 #
# bride building tools provided in this module:   #
#                                                 #
# for roadway surfaces:                           #
#                                                 #
#    singleSpanLightRoadwayLayer                  #
#    singleSpanHeavyRoadwayLayer                  #
#    doubleSpanLightRoadwayLayer                  #
#    doubleSpanHeavyRoadwayLayer                  #
#                                                 #
# for support layers                              #
#                                                 #
#    singleSpanSupportLayer                       #
#    doubleSpanSupportLayer                       #
#                                                 #
#                                                 #
###################################################
###################################################
# copyright 2013, Brooklyn Brige Building Company #
###################################################
###################################################


from lineSegments import *


###################################################
# tools for roadway surfaces:
###################################################

def singleSpanLightRoadwayLayer( ):
    '''
        returns a single span light roadway surface
    '''
    return line_segment_of_hyphens()   \
           + line_segment_of_hyphens() \
           + line_segment_of_hyphens()
    
def singleSpanHeavyRoadwayLayer( ):
    '''
        returns a single span heavy roadway surface
    '''
    return line_segment_of_equals()   \
           + line_segment_of_equals() \
           + line_segment_of_equals()
    
def doubleSpanLightRoadwayLayer( ):
    '''
        returns a double span light roadway surface
    '''
    return line_segment_of_hyphens()   \
           + line_segment_of_hyphens() \
           + line_segment_of_hyphens() \
           + line_segment_of_hyphens() \
           + line_segment_of_hyphens()
    
def doubleSpanHeavyRoadwayLayer( ):
    '''
        returns a double span heavy roadway surface
    '''
    return line_segment_of_equals()   \
           + line_segment_of_equals() \
           + line_segment_of_equals() \
           + line_segment_of_equals() \
           + line_segment_of_equals()
    
    
###################################################
# tools for support layers
###################################################

def singleSpanSupportLayer( ): 
    return line_segment_of_Xs()       \
           + line_segment_of_spaces() \
           + line_segment_of_Xs()
    
def doubleSpanSupportLayer( ): 
    return line_segment_of_Xs()       \
           + line_segment_of_spaces() \
           + line_segment_of_Xs()     \
           + line_segment_of_spaces() \
           + line_segment_of_Xs()

###################################################
###################################################
# copyright 2013, Brooklyn Brige Building Company #
###################################################
###################################################



   
    
