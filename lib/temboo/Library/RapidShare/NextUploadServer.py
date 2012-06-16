
###############################################################################
#
# NextUploadServer
# 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class NextUploadServer(Choreography):

    """
    Create a new instance of the NextUploadServer Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/NextUploadServer')


    def new_input_set(self):
        return NextUploadServerInputSet()

    def _make_result_set(self, result, path):
        return NextUploadServerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NextUploadServerChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the NextUploadServer
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class NextUploadServerInputSet(InputSet):
    pass

"""
A ResultSet with methods tailored to the values returned by the NextUploadServer choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class NextUploadServerResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ()
        """
        def get_Response(self):
            return self._output.get('Response', None)

class NextUploadServerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return NextUploadServerResultSet(response, path)
