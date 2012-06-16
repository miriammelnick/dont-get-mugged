
###############################################################################
#
# TrashDocumentOrFile
# Move the document or file you specify to the Google Documents trash.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TrashDocumentOrFile(Choreography):

    """
    Create a new instance of the TrashDocumentOrFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/TrashDocumentOrFile')


    def new_input_set(self):
        return TrashDocumentOrFileInputSet()

    def _make_result_set(self, result, path):
        return TrashDocumentOrFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrashDocumentOrFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TrashDocumentOrFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TrashDocumentOrFileInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The title of the document or file to trash. Enclose in quotation marks for an exact, non-case-sensitive match.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the TrashDocumentOrFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TrashDocumentOrFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "ResourceID" output from this choreography execution. ((string) The resource ID for the document to trash as returned by Google.)
        """
        def get_ResourceID(self):
            return self._output.get('ResourceID', None)

class TrashDocumentOrFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TrashDocumentOrFileResultSet(response, path)
