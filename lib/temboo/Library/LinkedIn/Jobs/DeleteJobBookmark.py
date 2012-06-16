
###############################################################################
#
# DeleteJobBookmark
# Delete a job bookmark by specifying a job ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteJobBookmark(Choreography):

    """
    Create a new instance of the DeleteJobBookmark Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Jobs/DeleteJobBookmark')


    def new_input_set(self):
        return DeleteJobBookmarkInputSet()

    def _make_result_set(self, result, path):
        return DeleteJobBookmarkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteJobBookmarkChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteJobBookmark
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteJobBookmarkInputSet(InputSet):
        """
        Set the value of the JobID input for this choreography. ((required, integer) Enter a LinkedIn job ID.)
        """
        def set_JobID(self, value):
            InputSet._set_input(self, 'JobID', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The Oauth Token Secret retrieved during the Oauth process.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Oauth Token retrieved during the Oauth process.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteJobBookmark choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteJobBookmarkResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from LinkedIn. Note that for a successful delete operation, no content is a returned and this output variable should be empty.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteJobBookmarkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteJobBookmarkResultSet(response, path)
