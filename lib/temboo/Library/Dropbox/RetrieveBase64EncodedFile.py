
###############################################################################
#
# RetrieveBase64EncodedFile
# Retrieves a file to your Dropbox account, and returns the file content as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveBase64EncodedFile(Choreography):

    """
    Create a new instance of the RetrieveBase64EncodedFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/RetrieveBase64EncodedFile')


    def new_input_set(self):
        return RetrieveBase64EncodedFileInputSet()

    def _make_result_set(self, result, path):
        return RetrieveBase64EncodedFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveBase64EncodedFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveBase64EncodedFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveBase64EncodedFileInputSet(InputSet):
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
        Set the value of the Path input for this choreography. ((required, string) The path to file you want to retrieve (i.e. RootFolder/SubFolder/MyFile.txt). Only the file name is necessary when the file is at the root level.)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveBase64EncodedFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveBase64EncodedFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from Dropbox. The response will contain the contents of the file you are retrieving as Base64 encoded data.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveBase64EncodedFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveBase64EncodedFileResultSet(response, path)
