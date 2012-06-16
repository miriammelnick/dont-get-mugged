
###############################################################################
#
# GetReportCount
# Retrieves the number of your available Amazon Marketplace reports, ready for download, that were generated in the last 90 days.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetReportCount(Choreography):

    """
    Create a new instance of the GetReportCount Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/GetReportCount')


    def new_input_set(self):
        return GetReportCountInputSet()

    def _make_result_set(self, result, path):
        return GetReportCountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReportCountChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetReportCount
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetReportCountInputSet(InputSet):
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
        Set the value of the Acknowledged input for this choreography. ((optional, boolean) A Boolean value that indicates if an order report has been acknowledged by a prior call to UpdateReportAcknowledgements. Set to "true" to list order reports that have been acknowledged.)
        """
        def set_Acknowledged(self, value):
            InputSet._set_input(self, 'Acknowledged', value)

        """
        Set the value of the AvailableFromDate input for this choreography. ((optional, date) The earliest date you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_AvailableFromDate(self, value):
            InputSet._set_input(self, 'AvailableFromDate', value)

        """
        Set the value of the AvailableToDate input for this choreography. ((optional, date) The most recent date you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_AvailableToDate(self, value):
            InputSet._set_input(self, 'AvailableToDate', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the ReportType input for this choreography. ((optional, string) A ReportType enumeration value (i.e. _GET_FLAT_FILE_OPEN_LISTINGS_DATA_).)
        """
        def set_ReportType(self, value):
            InputSet._set_input(self, 'ReportType', value)


"""
A ResultSet with methods tailored to the values returned by the GetReportCount choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetReportCountResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Count" output from this choreography execution. ((integer) A non-negative integer. parsed from the Amazon response, that represents the total number of reports available to download.)
        """
        def get_Count(self):
            return self._output.get('Count', None)

class GetReportCountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReportCountResultSet(response, path)
