
###############################################################################
#
# ViewDocument
# Lets you specify a document id to return information on a single document.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ViewDocument(Choreography):

    """
    Create a new instance of the ViewDocument Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OfficeDrop/ViewDocument')


    def new_input_set(self):
        return ViewDocumentInputSet()

    def _make_result_set(self, result, path):
        return ViewDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ViewDocumentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ViewDocument
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ViewDocumentInputSet(InputSet):
        """
        Set the value of the DocumentId input for this choreography. ((required, integer) The ID of the document you want to view.)
        """
        def set_DocumentId(self, value):
            InputSet._set_input(self, 'DocumentId', value)

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
A ResultSet with methods tailored to the values returned by the ViewDocument choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ViewDocumentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OfficeDrop.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ViewDocumentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ViewDocumentResultSet(response, path)
