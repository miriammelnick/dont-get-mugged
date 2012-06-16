
###############################################################################
#
# ValidateAddress
# Validates and supplements incomplete address information.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ValidateAddress(Choreography):

    """
    Create a new instance of the ValidateAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/USPS/AddressInformationAPI/ValidateAddress')


    def new_input_set(self):
        return ValidateAddressInputSet()

    def _make_result_set(self, result, path):
        return ValidateAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ValidateAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ValidateAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ValidateAddressInputSet(InputSet):
        """
        Set the value of the AptOrSuite input for this choreography. ((optional, string) Used to provide an apartment or suite number, if applicable. Maximum characters allowed: 38.)
        """
        def set_AptOrSuite(self, value):
            InputSet._set_input(self, 'AptOrSuite', value)

        """
        Set the value of the City input for this choreography. ((optional, string) Maximum characters allowed: 15. Either City and State or Zip are required.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the FirmName input for this choreography. ((optional, string) Maximum characters allowed: 38.)
        """
        def set_FirmName(self, value):
            InputSet._set_input(self, 'FirmName', value)

        """
        Set the value of the Password input for this choreography. ((string) The password assigned by USPS)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Maximum characters allowed: 2. Either City and State or Zip are required.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the StreetAddress input for this choreography. ((string) Street address. Maximum characters allowed: 38.)
        """
        def set_StreetAddress(self, value):
            InputSet._set_input(self, 'StreetAddress', value)

        """
        Set the value of the Urbanization input for this choreography. ((optional, string) Maximum characters allowed: 28. For Puerto Rico addresses only.)
        """
        def set_Urbanization(self, value):
            InputSet._set_input(self, 'Urbanization', value)

        """
        Set the value of the UserId input for this choreography. ((string) Alphanumeric ID assigned by USPS )
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)

        """
        Set the value of the Zip4DigitCode input for this choreography. ((optional, integer) Maximum characters allowed: 4)
        """
        def set_Zip4DigitCode(self, value):
            InputSet._set_input(self, 'Zip4DigitCode', value)

        """
        Set the value of the Zip input for this choreography. ((optional, integer) Maximum characters allowed: 5. Either City and State or Zip are required.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the ValidateAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ValidateAddressResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from USPS Web Service)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ValidateAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ValidateAddressResultSet(response, path)
