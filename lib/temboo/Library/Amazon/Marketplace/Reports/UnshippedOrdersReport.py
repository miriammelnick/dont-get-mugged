
###############################################################################
#
# UnshippedOrdersReport
# Returns a tab-delimited flat file report that contains only orders that are not confirmed as shipped.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UnshippedOrdersReport(Choreography):

    """
    Create a new instance of the UnshippedOrdersReport Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/UnshippedOrdersReport')


    def new_input_set(self):
        return UnshippedOrdersReportInputSet()

    def _make_result_set(self, result, path):
        return UnshippedOrdersReportResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnshippedOrdersReportChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UnshippedOrdersReport
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UnshippedOrdersReportInputSet(InputSet):
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
        Set the value of the TimeToWait input for this choreography. ((optional, integer) By default, the Choreo will wait for 5 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        def set_TimeToWait(self, value):
            InputSet._set_input(self, 'TimeToWait', value)


"""
A ResultSet with methods tailored to the values returned by the UnshippedOrdersReport choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UnshippedOrdersReportResultSet(ResultSet):
        """
        Retrieve the value for the "Report" output from this choreography execution. ((multiline) The report contents.)
        """
        def get_Report(self):
            return self._output.get('Report', None)
        """
        Retrieve the value for the "GeneratedReportId" output from this choreography execution. ((integer) The GeneratedReportId parsed from the Amazon response.)
        """
        def get_GeneratedReportId(self):
            return self._output.get('GeneratedReportId', None)
        """
        Retrieve the value for the "ReportProcessingStatus" output from this choreography execution. ((string) The status of the report request parsed from the Amazon response.)
        """
        def get_ReportProcessingStatus(self):
            return self._output.get('ReportProcessingStatus', None)
        """
        Retrieve the value for the "ReportRequestId" output from this choreography execution. ((integer) The ReportRequestId parsed from the Amazon response. This id is used in GetReportRequestList.)
        """
        def get_ReportRequestId(self):
            return self._output.get('ReportRequestId', None)

class UnshippedOrdersReportChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UnshippedOrdersReportResultSet(response, path)
