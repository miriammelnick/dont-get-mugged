
###############################################################################
#
# GetTopTags
# Retrieves the top tags used by a user. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTopTags(Choreography):

    """
    Create a new instance of the GetTopTags Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetTopTags')


    def new_input_set(self):
        return GetTopTagsInputSet()

    def _make_result_set(self, result, path):
        return GetTopTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopTagsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTopTags
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTopTagsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Limit the number of tags returned. Defaults to 10.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the User input for this choreography. ((string) The Last.fm username to fetch top tags for.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetTopTags choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTopTagsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTopTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopTagsResultSet(response, path)
