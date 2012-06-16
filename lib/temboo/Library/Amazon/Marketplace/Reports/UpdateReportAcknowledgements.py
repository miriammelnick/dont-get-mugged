
###############################################################################
#
# UpdateReportAcknowledgements
# Updates the acknowledged status of a report.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateReportAcknowledgements(Choreography):

    """
    Create a new instance of the UpdateReportAcknowledgements Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/UpdateReportAcknowledgements')


    def new_input_set(self):
        return UpdateReportAcknowledgementsInputSet()

    def _make_result_set(self, result, path):
        return UpdateReportAcknowledgementsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateReportAcknowledgementsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateReportAcknowledgements
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateReportAcknowledgementsInputSet(InputSet):
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
        Set the value of the Acknowledged input for this choreography. ((optional, boolean) A Boolean value that indicates if an order report has been acknowledged by a prior call to UpdateReportAcknowledgements. Set to true to list order reports that have been acknowledged.)
        """
        def set_Acknowledged(self, value):
            InputSet._set_input(self, 'Acknowledged', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the ReportId input for this choreography. ((required, integer) The id of the report to acknowledge.)
        """
        def set_ReportId(self, value):
            InputSet._set_input(self, 'ReportId', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateReportAcknowledgements choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateReportAcknowledgementsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateReportAcknowledgementsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateReportAcknowledgementsResultSet(response, path)
