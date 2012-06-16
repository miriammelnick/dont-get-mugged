
###############################################################################
#
# DeleteDocumentOrFile
# Permanently deletes the document or file you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteDocumentOrFile(Choreography):

    """
    Create a new instance of the DeleteDocumentOrFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/DeleteDocumentOrFile')


    def new_input_set(self):
        return DeleteDocumentOrFileInputSet()

    def _make_result_set(self, result, path):
        return DeleteDocumentOrFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDocumentOrFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteDocumentOrFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteDocumentOrFileInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ResourceID input for this choreography. ((required, string) The resource ID for the document or file to delete.)
        """
        def set_ResourceID(self, value):
            InputSet._set_input(self, 'ResourceID', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteDocumentOrFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteDocumentOrFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (There is no XML response for delete requests.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteDocumentOrFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDocumentOrFileResultSet(response, path)
