from lxml import etree
import dc_lxml_treesync as treesync
import pdb

Orig=r"""<dc:checklists xmlns:dc="http://thermal.cnde.iastate.edu/datacollect">
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="2014-11-29_40_files/chxexample_12-12345_.chf"/>
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="2014-11-29_40_files/chxexample_12-12345_-0001.chf"/>
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="mem://gavroche/1417290992/23950/33930704"/>
</dc:checklists>
"""

A=r"""<dc:checklists xmlns:dc="http://thermal.cnde.iastate.edu/datacollect">
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="2014-11-29_40_files/chxexample_12-12345_.chf"/>
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="2014-11-29_40_files/chxexample_12-12345_-0001.chf"/>
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="2014-11-29_40_files/chxexample_12-12345_-0002.chf"/>
</dc:checklists>

"""

B=r"""<dc:checklists xmlns:dc="http://thermal.cnde.iastate.edu/datacollect" xmlns:xlink="http://www.w3.org/1999/xlink">
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="2014-11-29_40_files/chxexample_12-12345_.chf"/>
  <dc:checklist xlink:href="2014-11-29_40_files/chxexample_12-12345_-000a.chf"/>
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="2014-11-29_40_files/chxexample_12-12345_-0001.chf"/>
  <dc:checklist xmlns:dbvar="http://thermal.cnde.iastate.edu/databrowse/variable" xmlns:sp="http://thermal.cnde.iastate.edu/spatial" xmlns:dcv="http://thermal.cnde.iastate.edu/dcvalue" xmlns:dcp="http://thermal.cnde.iastate.edu/datacollect/provenance" xmlns:chx="http://thermal.cnde.iastate.edu/checklist" xmlns:dbdir="http://thermal.cnde.iastate.edu/databrowse/dir" xlink:href="mem://gavroche/1417290992/23950/33930704"/>
</dc:checklists>
"""


tree_orig=etree.XML(Orig)
tree_A=etree.XML(A)
tree_B=etree.XML(B)
maxmergedepth=10

import pdb
try : 
    tree_merged=treesync.treesync(tree_orig,tree_A,tree_B,maxmergedepth,tag_index_paths_override={"{http://thermal.cnde.iastate.edu/datacollect}checklist":"@{http://www.w3.org/1999/xlink}href"})
    
    print(etree.tostring(tree_merged,pretty_print=True,encoding='utf-8').decode('utf-8'))
    
    tree_merged2=treesync.treesync_multi(tree_orig,[tree_A,tree_B],maxmergedepth,tag_index_paths_override={"{http://thermal.cnde.iastate.edu/datacollect}checklist":"@{http://www.w3.org/1999/xlink}href"})
    
    print(etree.tostring(tree_merged2,pretty_print=True,encoding='utf-8').decode('utf-8'))
except: 
    pdb.post_mortem()
    pass
