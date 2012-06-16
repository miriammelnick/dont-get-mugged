
###############################################################################
#
# GetMonthlyPayments
# Retrieve estimated monthly payments, including principal and interest based on current interest rates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetMonthlyPayments(Choreography):

    """
    Create a new instance of the GetMonthlyPayments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetMonthlyPayments')


    def new_input_set(self):
        return GetMonthlyPaymentsInputSet()

    def _make_result_set(self, result, path):
        return GetMonthlyPaymentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMonthlyPaymentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetMonthlyPayments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetMonthlyPaymentsInputSet(InputSet):
        """
        Set the value of the DollarsDown input for this choreography. ((optional, integer) Specify the dollar amount that is placed for a down payment. This variable can be used in place of DownPaymentAmount.)
        """
        def set_DollarsDown(self, value):
            InputSet._set_input(self, 'DollarsDown', value)

        """
        Set the value of the DownPaymentAmount input for this choreography. ((optional, integer) Enter the percentage of the total properly price that will be used as a down payment. If < 20%, mortage insurance info is also returned.)
        """
        def set_DownPaymentAmount(self, value):
            InputSet._set_input(self, 'DownPaymentAmount', value)

        """
        Set the value of the OutputFormat input for this choreography. ((optional, string) Enter the desired query output format.  Enter: xml, or json.  Default output is set to: xml.)
        """
        def set_OutputFormat(self, value):
            InputSet._set_input(self, 'OutputFormat', value)

        """
        Set the value of the Price input for this choreography. ((required, integer) Enter the price for which the monthly payment is to be calculated.)
        """
        def set_Price(self, value):
            InputSet._set_input(self, 'Price', value)

        """
        Set the value of the ZWSID input for this choreography. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        def set_ZWSID(self, value):
            InputSet._set_input(self, 'ZWSID', value)

        """
        Set the value of the Zip input for this choreography. ((optional, integer) Enter the zip code of the property.  If null, no property tax, or hazard insurance data will be returned.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the GetMonthlyPayments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetMonthlyPaymentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zillow.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetMonthlyPaymentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMonthlyPaymentsResultSet(response, path)
