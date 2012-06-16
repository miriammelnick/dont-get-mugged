
###############################################################################
#
# ListOrdersWithBuyerEmail
# Returns orders associated with a buyer's email address that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListOrdersWithBuyerEmail(Choreography):

    """
    Create a new instance of the ListOrdersWithBuyerEmail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Orders/ListOrdersWithBuyerEmail')


    def new_input_set(self):
        return ListOrdersWithBuyerEmailInputSet()

    def _make_result_set(self, result, path):
        return ListOrdersWithBuyerEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListOrdersWithBuyerEmailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListOrdersWithBuyerEmail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListOrdersWithBuyerEmailInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSMarketplaceId input for this choreography. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        def set_AWSMarketplaceId(self, value):
            InputSet._set_input(self, 'AWSMarketplaceId', value)

        """
        Set the value of the AWSMerchantId input for this choreography. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        def set_AWSMerchantId(self, value):
            InputSet._set_input(self, 'AWSMerchantId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the BuyerEmail input for this choreography. ((required, string) The e-mail address of a buyer. Used to select only the orders that contain the specified e-mail address.)
        """
        def set_BuyerEmail(self, value):
            InputSet._set_input(self, 'BuyerEmail', value)

        """
        Set the value of the CreatedAfter input for this choreography. ((optional, date) A date used for selecting orders created after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01). Defaults to today's date if not provided.)
        """
        def set_CreatedAfter(self, value):
            InputSet._set_input(self, 'CreatedAfter', value)

        """
        Set the value of the CreatedBefore input for this choreography. ((optional, date) A date used for selecting orders created before (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01).)
        """
        def set_CreatedBefore(self, value):
            InputSet._set_input(self, 'CreatedBefore', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the MaxResultsPerPage input for this choreography. ((optional, integer) A number that indicates the maximum number of orders that can be returned per page. Valid values are: 1-100.)
        """
        def set_MaxResultsPerPage(self, value):
            InputSet._set_input(self, 'MaxResultsPerPage', value)


"""
A ResultSet with methods tailored to the values returned by the ListOrdersWithBuyerEmail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListOrdersWithBuyerEmailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListOrdersWithBuyerEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListOrdersWithBuyerEmailResultSet(response, path)
