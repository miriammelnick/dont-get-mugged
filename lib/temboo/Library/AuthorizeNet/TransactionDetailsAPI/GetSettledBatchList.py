
###############################################################################
#
# GetSettledBatchList
# Returns data about a settled batch including: Batch ID, Settlement Time, and Settlement State, and Batch Statistics by payment type.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetSettledBatchList(Choreography):

    """
    Create a new instance of the GetSettledBatchList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AuthorizeNet/TransactionDetailsAPI/GetSettledBatchList')


    def new_input_set(self):
        return GetSettledBatchListInputSet()

    def _make_result_set(self, result, path):
        return GetSettledBatchListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSettledBatchListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetSettledBatchList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetSettledBatchListInputSet(InputSet):
        """
        Set the value of the APILoginId input for this choreography. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        def set_APILoginId(self, value):
            InputSet._set_input(self, 'APILoginId', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the FirstSettlementDate input for this choreography. ((required, date) Can be an epoch timestamp in milliseconds or formatted like 2010-12-01T00:00:00Z.)
        """
        def set_FirstSettlementDate(self, value):
            InputSet._set_input(self, 'FirstSettlementDate', value)

        """
        Set the value of the IncludeStatistics input for this choreography. ((optional, boolean) When 1 is specified, batch statistics by payment type are returned. Defaults to 1.)
        """
        def set_IncludeStatistics(self, value):
            InputSet._set_input(self, 'IncludeStatistics', value)

        """
        Set the value of the LastSettlementDate input for this choreography. ((required, date) Can be an epoch timestamp in milliseconds or formatted like 2010-12-01T00:00:00Z.)
        """
        def set_LastSettlementDate(self, value):
            InputSet._set_input(self, 'LastSettlementDate', value)

        """
        Set the value of the TransactionKey input for this choreography. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        def set_TransactionKey(self, value):
            InputSet._set_input(self, 'TransactionKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetSettledBatchList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetSettledBatchListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Authorize.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetSettledBatchListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSettledBatchListResultSet(response, path)
