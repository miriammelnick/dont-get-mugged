
###############################################################################
#
# PhotosFromUser
# Returns photos from a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PhotosFromUser(Choreography):

    """
    Create a new instance of the PhotosFromUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/PhotosFromUser')


    def new_input_set(self):
        return PhotosFromUserInputSet()

    def _make_result_set(self, result, path):
        return PhotosFromUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PhotosFromUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PhotosFromUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PhotosFromUserInputSet(InputSet):
        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to return, up to 500.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Used to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the UserID input for this choreography. ((optional, string) Identity of the user to get badges for. Defaults to "self" to get lists of the acting user.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the PhotosFromUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PhotosFromUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PhotosFromUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PhotosFromUserResultSet(response, path)
