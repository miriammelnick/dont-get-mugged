
###############################################################################
#
# DeletePost
# Deletes a specified post from a Tumblr blog.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeletePost(Choreography):

    """
    Create a new instance of the DeletePost Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/DeletePost')


    def new_input_set(self):
        return DeletePostInputSet()

    def _make_result_set(self, result, path):
        return DeletePostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePostChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeletePost
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeletePostInputSet(InputSet):
        """
        Set the value of the BaseHostname input for this choreography. ((string) The standard or custom blog hostname (i.e. temboo.tumblr.com))
        """
        def set_BaseHostname(self, value):
            InputSet._set_input(self, 'BaseHostname', value)

        """
        Set the value of the ID input for this choreography. ((integer) The ID of the post you want to delete)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((string) The Oauth Consumer Key provided by Tumblr after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((string) The Oauth Consumer Secret provided by Tumblr after registering your application)
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
A ResultSet with methods tailored to the values returned by the DeletePost choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeletePostResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Tumblr in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeletePostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeletePostResultSet(response, path)
