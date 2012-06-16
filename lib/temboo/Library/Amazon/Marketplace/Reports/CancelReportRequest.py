
###############################################################################
#
# CancelReportRequest
# Cancels one or more report requests.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CancelReportRequest(Choreography):

    """
    Create a new instance of the CancelReportRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/CancelReportRequest')


    def new_input_set(self):
        return CancelReportRequestInputSet()

    def _make_result_set(self, result, path):
        return CancelReportRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CancelReportRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CancelReportRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CancelReportRequestInputSet(InputSet):
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
        Set the value of the ReportProcessingStatus input for this choreography. ((optional, string) A report processing status by which to filter report requests. Valid values are: _SUBMITTED_, _IN_PROGRESS_, _CANCELLED_, _DONE_, _DONE_NO_DATA_.)
        """
        def set_ReportProcessingStatus(self, value):
            InputSet._set_input(self, 'ReportProcessingStatus', value)

        """
        Set the value of the ReportRequestId input for this choreography. ((optional, string) A ReportRequestId value. If you pass in a ReportRequestId value, other query conditions are ignored.)
        """
        def set_ReportRequestId(self, value):
            InputSet._set_input(self, 'ReportRequestId', value)

        """
        Set the value of the ReportType input for this choreography. ((optional, string) A ReportType enumeration value (i.e. GET_ORDERS_DATA_).)
        """
        def set_ReportType(self, value):
            InputSet._set_input(self, 'ReportType', value)

        """
        Set the value of the RequestedFromDate input for this choreography. ((optional, date) The start of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_RequestedFromDate(self, value):
            InputSet._set_input(self, 'RequestedFromDate', value)

        """
        Set the value of the RequestedToDate input for this choreography. ((optional, date) The end of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        def set_RequestedToDate(self, value):
            InputSet._set_input(self, 'RequestedToDate', value)


"""
A ResultSet with methods tailored to the values returned by the CancelReportRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CancelReportRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Count" output from this choreography execution. ((integer) A non-negative integer that represents the total number of report requests that were cancelled.)
        """
        def get_Count(self):
            return self._output.get('Count', None)

class CancelReportRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CancelReportRequestResultSet(response, path)
