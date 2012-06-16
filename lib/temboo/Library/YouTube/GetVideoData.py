
###############################################################################
#
# GetVideoData
# Retrieve information about a single video using its ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetVideoData(Choreography):

    """
    Create a new instance of the GetVideoData Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/YouTube/GetVideoData')


    def new_input_set(self):
        return GetVideoDataInputSet()

    def _make_result_set(self, result, path):
        return GetVideoDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetVideoDataChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetVideoData
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetVideoDataInputSet(InputSet):
        """
        Set the value of the VideoID input for this choreography. ((string) The unique ID given to a video by YouTube.)
        """
        def set_VideoID(self, value):
            InputSet._set_input(self, 'VideoID', value)


"""
A ResultSet with methods tailored to the values returned by the GetVideoData choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetVideoDataResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The result set returned by the API call.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetVideoDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetVideoDataResultSet(response, path)
