
###############################################################################
#
# TdocInclude
# 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TdocInclude(Choreography):

    """
    Create a new instance of the TdocInclude Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AccountService/Templates/TdocInclude')


    def new_input_set(self):
        return TdocIncludeInputSet()

    def _make_result_set(self, result, path):
        return TdocIncludeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TdocIncludeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TdocInclude
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TdocIncludeInputSet(InputSet):
    pass

"""
A ResultSet with methods tailored to the values returned by the TdocInclude choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TdocIncludeResultSet(ResultSet):
    pass

class TdocIncludeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TdocIncludeResultSet(response, path)
