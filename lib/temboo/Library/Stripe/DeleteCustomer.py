
###############################################################################
#
# DeleteCustomer
# Deletes a specified customer record.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteCustomer(Choreography):

    """
    Create a new instance of the DeleteCustomer Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/DeleteCustomer')


    def new_input_set(self):
        return DeleteCustomerInputSet()

    def _make_result_set(self, result, path):
        return DeleteCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCustomerChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteCustomer
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteCustomerInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the CustomerId input for this choreography. ((string) The unique identifier of the customer you want to delete)
        """
        def set_CustomerId(self, value):
            InputSet._set_input(self, 'CustomerId', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteCustomer choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteCustomerResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteCustomerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteCustomerResultSet(response, path)
