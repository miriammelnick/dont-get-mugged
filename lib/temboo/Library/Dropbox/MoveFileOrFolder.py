
###############################################################################
#
# MoveFileOrFolder
# Moves a file or folder to a new location in the Dropbox tree.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MoveFileOrFolder(Choreography):

    """
    Create a new instance of the MoveFileOrFolder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/MoveFileOrFolder')


    def new_input_set(self):
        return MoveFileOrFolderInputSet()

    def _make_result_set(self, result, path):
        return MoveFileOrFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MoveFileOrFolderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MoveFileOrFolder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MoveFileOrFolderInputSet(InputSet):
        """
        Set the value of the FromPath input for this choreography. ((required, string) Specifies the file or folder to be copied.)
        """
        def set_FromPath(self, value):
            InputSet._set_input(self, 'FromPath', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The OAuth Consumer Key provided by Dropbox after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Drop Box after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The OAuth Token Secret retrieved during the OAuth process.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The OAuth Token retrieved during the OAuth process.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the ToPath input for this choreography. ((required, string) Specifies the destination path, including the new name for the file or folder.)
        """
        def set_ToPath(self, value):
            InputSet._set_input(self, 'ToPath', value)


"""
A ResultSet with methods tailored to the values returned by the MoveFileOrFolder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MoveFileOrFolderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MoveFileOrFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MoveFileOrFolderResultSet(response, path)
