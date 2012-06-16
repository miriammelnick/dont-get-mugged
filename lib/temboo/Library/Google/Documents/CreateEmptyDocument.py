
###############################################################################
#
# CreateEmptyDocument
# Create a new, empty document.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateEmptyDocument(Choreography):

    """
    Create a new instance of the CreateEmptyDocument Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/CreateEmptyDocument')


    def new_input_set(self):
        return CreateEmptyDocumentInputSet()

    def _make_result_set(self, result, path):
        return CreateEmptyDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEmptyDocumentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateEmptyDocument
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateEmptyDocumentInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The title of the new document to create.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the CreateEmptyDocument choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateEmptyDocumentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "EditLink" output from this choreography execution. (The edit link URL parsed from the Google response.)
        """
        def get_EditLink(self):
            return self._output.get('EditLink', None)
        """
        Retrieve the value for the "ResourceID" output from this choreography execution. ((string) The document resource ID returned from Google.)
        """
        def get_ResourceID(self):
            return self._output.get('ResourceID', None)

class CreateEmptyDocumentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEmptyDocumentResultSet(response, path)
