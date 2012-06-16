
###############################################################################
#
# RetrieveInvoice
# Retrieves invoice details using the invoice id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveInvoice(Choreography):

    """
    Create a new instance of the RetrieveInvoice Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Stripe/RetrieveInvoice')


    def new_input_set(self):
        return RetrieveInvoiceInputSet()

    def _make_result_set(self, result, path):
        return RetrieveInvoiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveInvoiceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveInvoice
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveInvoiceInputSet(InputSet):
        """
        Set the value of the APISecretKey input for this choreography. ((string) The secret API Key providied by Stripe)
        """
        def set_APISecretKey(self, value):
            InputSet._set_input(self, 'APISecretKey', value)

        """
        Set the value of the InvoiceId input for this choreography. ((string) The unique identifier of the invoice you want to retrieve)
        """
        def set_InvoiceId(self, value):
            InputSet._set_input(self, 'InvoiceId', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveInvoice choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveInvoiceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Stripe)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveInvoiceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveInvoiceResultSet(response, path)
