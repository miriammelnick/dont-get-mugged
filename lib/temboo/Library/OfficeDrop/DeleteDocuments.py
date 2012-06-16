
###############################################################################
#
# DeleteDocuments
# Lets you move documents to the trash by specifying document ids.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteDocuments(Choreography):

    """
    Create a new instance of the DeleteDocuments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OfficeDrop/DeleteDocuments')


    def new_input_set(self):
        return DeleteDocumentsInputSet()

    def _make_result_set(self, result, path):
        return DeleteDocumentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDocumentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteDocuments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteDocumentsInputSet(InputSet):
        """
        Set the value of the DocumentIds input for this choreography. ((required, integer) The IDs of the documents you want to move to the trash.  Separate IDs by commas.)
        """
        def set_DocumentIds(self, value):
            InputSet._set_input(self, 'DocumentIds', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your OfficeDrop password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your OfficeDrop username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteDocuments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteDocumentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OfficeDrop.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteDocumentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDocumentsResultSet(response, path)
