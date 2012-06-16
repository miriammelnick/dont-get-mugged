
###############################################################################
#
# SearchFilesAndFolders
# Allows you to search Dropbox for files or folders by a keyword search.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchFilesAndFolders(Choreography):

    """
    Create a new instance of the SearchFilesAndFolders Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/SearchFilesAndFolders')


    def new_input_set(self):
        return SearchFilesAndFoldersInputSet()

    def _make_result_set(self, result, path):
        return SearchFilesAndFoldersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchFilesAndFoldersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchFilesAndFolders
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchFilesAndFoldersInputSet(InputSet):
        """
        Set the value of the FileLimit input for this choreography. ((optional, integer) Dropbox will not return a list that exceeds this specified limit. Defaults to 10,000.)
        """
        def set_FileLimit(self, value):
            InputSet._set_input(self, 'FileLimit', value)

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
        Set the value of the Path input for this choreography. ((optional, string) The path to the folder you want to search from (i.e. RootFolder/SubFolder). Leave blank to search ALL.)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the Query input for this choreography. ((required, string) The search string. Must be at least three characters long.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the SearchFilesAndFolders choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchFilesAndFoldersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchFilesAndFoldersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchFilesAndFoldersResultSet(response, path)
