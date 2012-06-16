
###############################################################################
#
# GetTransactionList
# Returns a list of transactions and their details for a specified batch ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTransactionList(Choreography):

    """
    Create a new instance of the GetTransactionList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AuthorizeNet/TransactionDetailsAPI/GetTransactionList')


    def new_input_set(self):
        return GetTransactionListInputSet()

    def _make_result_set(self, result, path):
        return GetTransactionListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTransactionListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTransactionList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTransactionListInputSet(InputSet):
        """
        Set the value of the APILoginId input for this choreography. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        def set_APILoginId(self, value):
            InputSet._set_input(self, 'APILoginId', value)

        """
        Set the value of the BatchId input for this choreography. ((required, integer) The id of the batch that you want to retrieve a list of transactions for.)
        """
        def set_BatchId(self, value):
            InputSet._set_input(self, 'BatchId', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the TransactionKey input for this choreography. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        def set_TransactionKey(self, value):
            InputSet._set_input(self, 'TransactionKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetTransactionList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTransactionListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Authorize.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTransactionListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTransactionListResultSet(response, path)
