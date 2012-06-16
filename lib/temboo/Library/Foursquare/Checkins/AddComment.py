
###############################################################################
#
# AddComment
# Adds a comment to a specified checkin.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddComment(Choreography):

    """
    Create a new instance of the AddComment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/AddComment')


    def new_input_set(self):
        return AddCommentInputSet()

    def _make_result_set(self, result, path):
        return AddCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddCommentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddComment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddCommentInputSet(InputSet):
        """
        Set the value of the CheckinID input for this choreography. ((required, string) The ID of the checkin that you want to create a comment for.)
        """
        def set_CheckinID(self, value):
            InputSet._set_input(self, 'CheckinID', value)

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
        Set the value of the Text input for this choreography. ((required, string) The text of the comment, up to 200 characters.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)


"""
A ResultSet with methods tailored to the values returned by the AddComment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddCommentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddCommentResultSet(response, path)
