
###############################################################################
#
# GetAllDocuments
# Retrieves a list of all documents, files, and collections in a Google account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAllDocuments(Choreography):

    """
    Create a new instance of the GetAllDocuments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/GetAllDocuments')


    def new_input_set(self):
        return GetAllDocumentsInputSet()

    def _make_result_set(self, result, path):
        return GetAllDocumentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllDocumentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAllDocuments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAllDocumentsInputSet(InputSet):
        """
        Set the value of the Deleted input for this choreography. ((optional, boolean) Returns deleted documents when set to "true" (the default). Skips deleted documents when set to "false".)
        """
        def set_Deleted(self, value):
            InputSet._set_input(self, 'Deleted', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetAllDocuments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAllDocumentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAllDocumentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllDocumentsResultSet(response, path)
