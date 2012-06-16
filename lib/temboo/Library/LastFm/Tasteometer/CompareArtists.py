
###############################################################################
#
# CompareArtists
# Retrieves a Tasteometer score from two artist inputs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CompareArtists(Choreography):

    """
    Create a new instance of the CompareArtists Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Tasteometer/CompareArtists')


    def new_input_set(self):
        return CompareArtistsInputSet()

    def _make_result_set(self, result, path):
        return CompareArtistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompareArtistsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CompareArtists
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CompareArtistsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Artist1 input for this choreography. ((string) The first artist to compare.)
        """
        def set_Artist1(self, value):
            InputSet._set_input(self, 'Artist1', value)

        """
        Set the value of the Artist2 input for this choreography. ((string) The second artist to compare.)
        """
        def set_Artist2(self, value):
            InputSet._set_input(self, 'Artist2', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) How many shared artists to display. Defaults to 5.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)


"""
A ResultSet with methods tailored to the values returned by the CompareArtists choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CompareArtistsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CompareArtistsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompareArtistsResultSet(response, path)
