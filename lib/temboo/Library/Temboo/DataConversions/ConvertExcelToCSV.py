
###############################################################################
#
# ConvertExcelToCSV
# Converts Excel (.xls) formatted data to CSV.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ConvertExcelToCSV(Choreography):

    """
    Create a new instance of the ConvertExcelToCSV Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/DataConversions/ConvertExcelToCSV')


    def new_input_set(self):
        return ConvertExcelToCSVInputSet()

    def _make_result_set(self, result, path):
        return ConvertExcelToCSVResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertExcelToCSVChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ConvertExcelToCSV
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ConvertExcelToCSVInputSet(InputSet):
        """
        Set the value of the ExcelFile input for this choreography. ((conditional, string) The base64-encoded contents of the Excel file that you want to convert to CSV. Required unless using the VaultFile input alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_ExcelFile(self, value):
            InputSet._set_input(self, 'ExcelFile', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) A path to an Excel file you've stored in the Vault. This can be used as an alternative to the ExcelFile input variable.)
        """


"""
A ResultSet with methods tailored to the values returned by the ConvertExcelToCSV choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ConvertExcelToCSVResultSet(ResultSet):
        """
        Retrieve the value for the "CSVFile" output from this choreography execution. ((string) The CSV formatted data.)
        """
        def get_CSVFile(self):
            return self._output.get('CSVFile', None)

class ConvertExcelToCSVChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConvertExcelToCSVResultSet(response, path)
