
###############################################################################
#
# AddOrUpdateInventoryItems
# Adds or updates one or more inventory listings in your Seller Central account with a given flat flile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddOrUpdateInventoryItems(Choreography):

    """
    Create a new instance of the AddOrUpdateInventoryItems Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/AddOrUpdateInventoryItems')


    def new_input_set(self):
        return AddOrUpdateInventoryItemsInputSet()

    def _make_result_set(self, result, path):
        return AddOrUpdateInventoryItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddOrUpdateInventoryItemsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddOrUpdateInventoryItems
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddOrUpdateInventoryItemsInputSet(InputSet):
        """
        Set the value of the FeedData input for this choreography. ((conditional, multiline) The feed data to sumbit to Amazon Marketplace.)
        """
        def set_FeedData(self, value):
            InputSet._set_input(self, 'FeedData', value)

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
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the TimeToWait input for this choreography. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        def set_TimeToWait(self, value):
            InputSet._set_input(self, 'TimeToWait', value)

        """
        Set the value of the VaultFile input for this choreography. (The path to the vault file you want to submit. Required unless you using the FeedData input.)
        """


"""
A ResultSet with methods tailored to the values returned by the AddOrUpdateInventoryItems choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddOrUpdateInventoryItemsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon after submitting the feed.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "ProcessingStatus" output from this choreography execution. ((string) The processing status of the feed submission which is parsed from the Amazon response.)
        """
        def get_ProcessingStatus(self):
            return self._output.get('ProcessingStatus', None)
        """
        Retrieve the value for the "SubmissionId" output from this choreography execution. ((integer) The submission id parsed from the Amazon response.)
        """
        def get_SubmissionId(self):
            return self._output.get('SubmissionId', None)
        """
        Retrieve the value for the "SubmissionResult" output from this choreography execution. ((string) The submission result returned from Amazon.)
        """
        def get_SubmissionResult(self):
            return self._output.get('SubmissionResult', None)

class AddOrUpdateInventoryItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddOrUpdateInventoryItemsResultSet(response, path)
