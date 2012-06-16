
###############################################################################
#
# ConvertCSVToBase64EncodedExcel
# Converts a CSV formatted file to Base64 encoded Excel data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ConvertCSVToBase64EncodedExcel(Choreography):

    """
    Create a new instance of the ConvertCSVToBase64EncodedExcel Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/DataConversions/ConvertCSVToBase64EncodedExcel')


    def new_input_set(self):
        return ConvertCSVToBase64EncodedExcelInputSet()

    def _make_result_set(self, result, path):
        return ConvertCSVToBase64EncodedExcelResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertCSVToBase64EncodedExcelChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ConvertCSVToBase64EncodedExcel
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ConvertCSVToBase64EncodedExcelInputSet(InputSet):
        """
        Set the value of the CSVFile input for this choreography. ((conditional, multiline) The CSV data you want to convert to XLS format. Required unless using the VaultFile input alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_CSVFile(self, value):
            InputSet._set_input(self, 'CSVFile', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) A path to a CSV file you've stored in the Vault. This can be used as an alternative to the CSVFile input variable.)
        """


"""
A ResultSet with methods tailored to the values returned by the ConvertCSVToBase64EncodedExcel choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ConvertCSVToBase64EncodedExcelResultSet(ResultSet):
        """
        Retrieve the value for the "ExcelFile" output from this choreography execution. ((string) The Base64 encoded Excel data.)
        """
        def get_ExcelFile(self):
            return self._output.get('ExcelFile', None)

class ConvertCSVToBase64EncodedExcelChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConvertCSVToBase64EncodedExcelResultSet(response, path)
