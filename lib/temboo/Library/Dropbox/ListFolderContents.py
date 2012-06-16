
###############################################################################
#
# ListFolderContents
# Lists contents of a given Dropbox folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListFolderContents(Choreography):

    """
    Create a new instance of the ListFolderContents Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/ListFolderContents')


    def new_input_set(self):
        return ListFolderContentsInputSet()

    def _make_result_set(self, result, path):
        return ListFolderContentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListFolderContentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListFolderContents
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListFolderContentsInputSet(InputSet):
        """
        Set the value of the FileLimit input for this choreography. ((optional, integer) Dropbox will not return a list that exceeds this specified limit. Defaults to 10,000.)
        """
        def set_FileLimit(self, value):
            InputSet._set_input(self, 'FileLimit', value)

        """
        Set the value of the Folder input for this choreography. ((optional, string) The name of the folder that contains the listing you want to retrieve. A path to a sub-folder is also valid (i.e. RootFolder/SubFolder).)
        """
        def set_Folder(self, value):
            InputSet._set_input(self, 'Folder', value)

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
A ResultSet with methods tailored to the values returned by the ListFolderContents choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListFolderContentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListFolderContentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListFolderContentsResultSet(response, path)
