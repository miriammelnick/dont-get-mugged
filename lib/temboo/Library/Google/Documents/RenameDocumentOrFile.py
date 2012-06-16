
###############################################################################
#
# RenameDocumentOrFile
# Rename a document or file with the new title you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RenameDocumentOrFile(Choreography):

    """
    Create a new instance of the RenameDocumentOrFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/RenameDocumentOrFile')


    def new_input_set(self):
        return RenameDocumentOrFileInputSet()

    def _make_result_set(self, result, path):
        return RenameDocumentOrFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RenameDocumentOrFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RenameDocumentOrFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RenameDocumentOrFileInputSet(InputSet):
        """
        Set the value of the NewTitle input for this choreography. ((required, string) The new title for the document. It will appear exactly as you type it, so be sure to use the proper capitalization.)
        """
        def set_NewTitle(self, value):
            InputSet._set_input(self, 'NewTitle', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The title of the document to rename.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the RenameDocumentOrFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RenameDocumentOrFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "EditLink" output from this choreography execution. ((string) The edit link URL for the document to rename, parsed from the Google response.)
        """
        def get_EditLink(self):
            return self._output.get('EditLink', None)

class RenameDocumentOrFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RenameDocumentOrFileResultSet(response, path)
