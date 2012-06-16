
###############################################################################
#
# RequestReport
# Creates a report request and submits the request to Amazon MWS.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RequestReport(Choreography):

    """
    Create a new instance of the RequestReport Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/RequestReport')


    def new_input_set(self):
        return RequestReportInputSet()

    def _make_result_set(self, result, path):
        return RequestReportResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RequestReportChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RequestReport
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RequestReportInputSet(InputSet):
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
        Set the value of the EndDate input for this choreography. ((optional, date) The end of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the ReportOptions input for this choreography. ((optional, string) A Boolean value that shows or hides an additional column of information on several order reports. When set to ShowSalesChannel=true, an additional column is added showing the sales channel.)
        """
        def set_ReportOptions(self, value):
            InputSet._set_input(self, 'ReportOptions', value)

        """
        Set the value of the ReportType input for this choreography. ((optional, string) A ReportType enumeration value. Defaults to _GET_FLAT_FILE_OPEN_LISTINGS_DATA_.)
        """
        def set_ReportType(self, value):
            InputSet._set_input(self, 'ReportType', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, date) The start of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)


"""
A ResultSet with methods tailored to the values returned by the RequestReport choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RequestReportResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
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

class RequestReportChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RequestReportResultSet(response, path)
