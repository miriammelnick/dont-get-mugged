
###############################################################################
#
# UpdateInvoiceItem
# Updates the amount or description of an existing invoice item.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateInvoiceItem(Choreography):

    """
    Create a new instance of the UpdateInvoiceItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/UpdateInvoiceItem')


    def new_input_set(self):
        return UpdateInvoiceItemInputSet()

    def _make_result_set(self, result, path):
        return UpdateInvoiceItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateInvoiceItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateInvoiceItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateInvoiceItemInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the Amount input for this choreography. ((integer) The amount in cents of the charge to be included in the customer's next invoice)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the Currency input for this choreography. ((optional, string) 3-letter ISO code for currency. Defaults to 'usd' which is currently the only supported currency.)
        """
        def set_Currency(self, value):
            InputSet._set_input(self, 'Currency', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) An arbitrary string of text that will be included with the invoice item)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the InvoiceItemId input for this choreography. ((string) The unique identifier of the invoice item you want to update)
        """
        def set_InvoiceItemId(self, value):
            InputSet._set_input(self, 'InvoiceItemId', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateInvoiceItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateInvoiceItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Description" output from this choreography execution. ((optional, string) An arbitrary string of text that will be included with the invoice item)
        """
        def get_Description(self):
            return self._output.get('Description', None)

class UpdateInvoiceItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateInvoiceItemResultSet(response, path)
