
###############################################################################
#
# GetCorrection
# Allows you to check whether the supplied artist has a correction to a canonical artist.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCorrection(Choreography):

    """
    Create a new instance of the GetCorrection Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Artist/GetCorrection')


    def new_input_set(self):
        return GetCorrectionInputSet()

    def _make_result_set(self, result, path):
        return GetCorrectionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCorrectionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCorrection
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCorrectionInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Artist input for this choreography. ((string) The artist name to correct.)
        """
        def set_Artist(self, value):
            InputSet._set_input(self, 'Artist', value)


"""
A ResultSet with methods tailored to the values returned by the GetCorrection choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCorrectionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCorrectionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCorrectionResultSet(response, path)
