
###############################################################################
#
# UnfollowList
# Allows a user to unfollow a list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UnfollowList(Choreography):

    """
    Create a new instance of the UnfollowList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/UnfollowList')


    def new_input_set(self):
        return UnfollowListInputSet()

    def _make_result_set(self, result, path):
        return UnfollowListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnfollowListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UnfollowList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UnfollowListInputSet(InputSet):
        """
        Set the value of the ListID input for this choreography. ((required, string) The id of a user-created list.)
        """
        def set_ListID(self, value):
            InputSet._set_input(self, 'ListID', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the UnfollowList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UnfollowListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UnfollowListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UnfollowListResultSet(response, path)
