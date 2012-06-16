
###############################################################################
#
# DownloadBase64EncodedDocument
# Downloads a document with the title you specify, and returns the content as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DownloadBase64EncodedDocument(Choreography):

    """
    Create a new instance of the DownloadBase64EncodedDocument Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/DownloadBase64EncodedDocument')


    def new_input_set(self):
        return DownloadBase64EncodedDocumentInputSet()

    def _make_result_set(self, result, path):
        return DownloadBase64EncodedDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadBase64EncodedDocumentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DownloadBase64EncodedDocument
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DownloadBase64EncodedDocumentInputSet(InputSet):
        """
        Set the value of the Format input for this choreography. ((optional, string) The format you want to export the document to, such as "doc", "txt", "pdf", etc. The default download format is HTML.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the Link input for this choreography. ((conditional, string) Enter the source links for the document to be retrieved. Required unless specifying the Title.)
        """
        def set_Link(self, value):
            InputSet._set_input(self, 'Link', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((conditional, string) The title of the document to download. Required unless specifying the download Link.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DownloadBase64EncodedDocument choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DownloadBase64EncodedDocumentResultSet(ResultSet):
        """
        Retrieve the value for the "FileContents" output from this choreography execution. ((string) The Base64 encoded file content of the downloaded file.)
        """
        def get_FileContents(self):
            return self._output.get('FileContents', None)

class DownloadBase64EncodedDocumentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DownloadBase64EncodedDocumentResultSet(response, path)
