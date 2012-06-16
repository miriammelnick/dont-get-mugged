
###############################################################################
#
# DeleteInvoiceItem
# Deletes a specified invoice item.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteInvoiceItem(Choreography):

    """
    Create a new instance of the DeleteInvoiceItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/DeleteInvoiceItem')


    def new_input_set(self):
        return DeleteInvoiceItemInputSet()

    def _make_result_set(self, result, path):
        return DeleteInvoiceItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteInvoiceItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteInvoiceItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteInvoiceItemInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the InvoiceItemId input for this choreography. ((string) The unique identifier of the invoice item you want to delete)
        """
        def set_InvoiceItemId(self, value):
            InputSet._set_input(self, 'InvoiceItemId', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteInvoiceItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteInvoiceItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteInvoiceItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteInvoiceItemResultSet(response, path)
