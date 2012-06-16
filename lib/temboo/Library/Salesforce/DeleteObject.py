
###############################################################################
#
# DeleteObject
# Deletes a specified Salesforce Object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteObject(Choreography):

    """
    Create a new instance of the DeleteObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Salesforce/DeleteObject')


    def new_input_set(self):
        return DeleteObjectInputSet()

    def _make_result_set(self, result, path):
        return DeleteObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteObjectInputSet(InputSet):
        """
        Set the value of the ID input for this choreography. ((required, string) The ID of the Object you wish to delete)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Salesforce password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SecurityToken input for this choreography. ((required, string) Your Salesforce security token used for API calls.)
        """
        def set_SecurityToken(self, value):
            InputSet._set_input(self, 'SecurityToken', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Salesforce username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The full response from Salesforce)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteObjectResultSet(response, path)
