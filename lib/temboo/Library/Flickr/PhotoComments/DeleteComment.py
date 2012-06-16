
###############################################################################
#
# DeleteComment
# Delete a specified comment from a photo on Flickr.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteComment(Choreography):

    """
    Create a new instance of the DeleteComment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/PhotoComments/DeleteComment')


    def new_input_set(self):
        return DeleteCommentInputSet()

    def _make_result_set(self, result, path):
        return DeleteCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCommentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteComment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteCommentInputSet(InputSet):
        """
        Set the value of the CommentId input for this choreography. ((string) The unique id of the comment that you want to delete)
        """
        def set_CommentId(self, value):
            InputSet._set_input(self, 'CommentId', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((string) The Oauth Consumer Key provided by Flickr after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((string) The Oauth Consumer Secret provided by Flickr after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((string) The Oauth Token Secret retrieved during the Oauth process)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((string) The Oauth Token retrieved during the Oauth process)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteComment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteCommentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Flickr)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteCommentResultSet(response, path)
